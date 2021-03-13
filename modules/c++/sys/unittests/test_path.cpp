/* =========================================================================
 * This file is part of sys-c++
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2016, MDA Information Systems LLC
 *
 * sys-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; If not, 
 * see <http://www.gnu.org/licenses/>.
 *
 */

#include <assert.h>

#include <sys/Path.h>
#include "TestCase.h"

namespace
{
TEST_CASE(testPathMerge)
{
    const sys::OS os;

    // PATH is usually set to multiple directories on both Windows and *nix
    std::vector<std::string> paths;
    const auto splitResult = os.splitEnv("PATH", paths);
    TEST_ASSERT_TRUE(splitResult);
    TEST_ASSERT_GREATER(paths.size(), 0);

    std::string path;
    for (const auto& p : paths)
    {
        if (sys::Filesystem::is_directory(p))
        {
            path = p;
            break;
        }
    }
    TEST_ASSERT_TRUE(sys::Filesystem::is_directory(path));

    bool isAbsolute;
    auto components = sys::Path::separate(path, isAbsolute);
    TEST_ASSERT_GREATER(components.size(), 0);
    auto result = sys::Path::merge(components, isAbsolute);
    TEST_ASSERT_EQ(result, path);
    TEST_ASSERT_TRUE(sys::Filesystem::is_directory(result));

    #if _WIN32
    path = R"(\\server\dir\file.txt)";
    #else
    path = R"(/dir1/dir2/file.txt)";
    #endif
    components = sys::Path::separate(path, isAbsolute);
    TEST_ASSERT_EQ(components.size(), 3);
    result = sys::Path::merge(components, isAbsolute);
    TEST_ASSERT_EQ(result, path);
}

TEST_CASE(testExpandEnvTilde)
{
    auto path = sys::Path::expandEnvironmentVariables("~");
    TEST_ASSERT_TRUE(sys::Filesystem::is_directory(path));

    path = sys::Path::expandEnvironmentVariables("~", sys::Filesystem::FileType::Directory);
    TEST_ASSERT_TRUE(sys::Filesystem::is_directory(path));

    path = sys::Path::expandEnvironmentVariables("~", sys::Filesystem::FileType::Regular);
    TEST_ASSERT_TRUE(path.empty());
}

TEST_CASE(testExpandEnvPath)
{
    const auto path = sys::Path::expandEnvironmentVariables("$PATH", false);
    TEST_ASSERT_FALSE(path.empty());

    #if _WIN32  // %FOO% only on Windows
    const auto win32_path = sys::Path::expandEnvironmentVariables("%PATH%", false);
    TEST_ASSERT_EQ(win32_path, path);
    #endif

    const auto path2 = sys::Path::expandEnvironmentVariables("$(PATH)", false);
    TEST_ASSERT_EQ(path2, path);

    const auto path3 = sys::Path::expandEnvironmentVariables("${PATH}", false);
    TEST_ASSERT_EQ(path3, path);

    const auto foopath = sys::Path::expandEnvironmentVariables("foo${PATH}", false);
    TEST_ASSERT_EQ(foopath, "foo" + path);

    const auto pathfoo = sys::Path::expandEnvironmentVariables("${PATH}foo", false);
    TEST_ASSERT_EQ(pathfoo, path + "foo");

    const auto foopathbar = sys::Path::expandEnvironmentVariables("foo${PATH}bar", false);
    TEST_ASSERT_EQ(foopathbar, "foo" + path + "bar");

    const auto foopath_bar = sys::Path::expandEnvironmentVariables("foo$PATH-bar", false);
    TEST_ASSERT_EQ(foopath_bar, "foo" + path + "-bar");

    auto foopath_bar_ = sys::Path::expandEnvironmentVariables("foo$PATH(bar)", false);
    TEST_ASSERT_FALSE(foopath_bar_.empty());
    TEST_ASSERT_EQ(foopath_bar_, "foo" + path + "(bar)");

    foopath_bar_ = sys::Path::expandEnvironmentVariables("foo$PATH)bar(", false);
    TEST_ASSERT_EQ(foopath_bar_, "foo" + path + ")bar(");

    foopath_bar_ = sys::Path::expandEnvironmentVariables("foo$(PATH)BAR)", false);
    TEST_ASSERT_EQ(foopath_bar_, "foo" + path + "BAR)");

    auto pathpath = sys::Path::expandEnvironmentVariables("$PATH$PATH", false);
    TEST_ASSERT_EQ(pathpath, path + path);
    #if _WIN32  // %FOO% only on Windows
    pathpath = sys::Path::expandEnvironmentVariables("%PATH%%PATH%", false);
    TEST_ASSERT_EQ(pathpath, path + path);
    #endif

    const auto foopath_barpathbar_ = sys::Path::expandEnvironmentVariables("foo$PATH-bar$(PATH)BAR)", false);
    TEST_ASSERT_EQ(foopath_barpathbar_, "foo" + path + "-bar" + path + "BAR)");
}

TEST_CASE(testExpandEnvPathExists)
{
    sys::OS os;
    #ifdef _WIN32
    const std::string does_not_exist(R"(Q:\Does\Not\Exist)");
    #else
    const std::string does_not_exist(R"(/does/not/existt)");
    #endif
    std::vector<std::string> values{does_not_exist};
    bool result = os.prependEnv("PATH", values, true /*overwrite*/);
    TEST_ASSERT_TRUE(result);

    const auto path = sys::Path::expandEnvironmentVariables("$PATH");
    TEST_ASSERT_FALSE(path.empty());

    #if _WIN32  // %FOO% only on Windows
    const auto win32_path = sys::Path::expandEnvironmentVariables("%PATH%");
    TEST_ASSERT_EQ(win32_path, path);
    #endif

    const auto path2 = sys::Path::expandEnvironmentVariables("$(PATH)");
    TEST_ASSERT_EQ(path2, path);

    const auto path3 = sys::Path::expandEnvironmentVariables("${PATH}");
    TEST_ASSERT_EQ(path3, path);
}

TEST_CASE(testExpandEnvPathMultiple)
{
    sys::OS os;

    const std::vector<std::string> paths{"home", "opt", "var"};
    bool result = os.prependEnv("paths", paths, false /*overwrite*/);
    TEST_ASSERT_TRUE(result);
    const std::vector<std::string> apps{"apps"};
    result = os.prependEnv("apps", apps, false /*overwrite*/);
    TEST_ASSERT_TRUE(result);
    const std::vector<std::string> app{"app_v1", "app_v2"};
    result = os.prependEnv("app", app, false /*overwrite*/);
    TEST_ASSERT_TRUE(result);
    const std::vector<std::string> libs{"lib", "lib64"};
    result = os.prependEnv("libs", libs, false /*overwrite*/);
    TEST_ASSERT_TRUE(result);
    const std::vector<std::string> exts{"libfoo.a", "libfoo.so", "foo.dll"};
    result = os.prependEnv("exts", exts, false /*overwrite*/);
    TEST_ASSERT_TRUE(result);

    const std::string path_to_expand = "/disk0/$(paths)/$(apps)/$(app)/$(libs)/$(exts)";
    const std::vector<std::string> expected{"disk0", paths[0], apps[0], app[0], libs[0], exts[0]};
    auto expected_path = sys::Path::merge(expected, true /*isAbsolute*/);
    auto expanded_path = sys::Path::expandEnvironmentVariables(path_to_expand, false /*checkIfExists*/);
    TEST_ASSERT_EQ(expanded_path, expected_path);

    const auto expanded_paths = sys::Path::expandedEnvironmentVariables(path_to_expand);
    TEST_ASSERT_EQ(expanded_paths.size(), paths.size() * apps.size() * app.size() * libs.size() * exts.size());
    const std::vector<std::string> expected_back{"disk0", paths.back(), apps.back(), app.back(), libs.back(), exts.back()};
    expected_path = sys::Path::merge(expected_back, true /*isAbsolute*/);
    TEST_ASSERT_EQ(expanded_paths.back(), expected_path);
}

}

int main(int, char**)
{
    TEST_CHECK(testPathMerge);
    TEST_CHECK(testExpandEnvTilde);
    TEST_CHECK(testExpandEnvPath);
    TEST_CHECK(testExpandEnvPathExists);
    TEST_CHECK(testExpandEnvPathMultiple);

    return 0;
}

