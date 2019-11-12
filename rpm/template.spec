%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-ainstein-radar
Version:        2.0.1
Release:        1%{?dist}
Summary:        ROS ainstein_radar package

License:        BSD
URL:            https://wiki.ros.org/ainstein_radar
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-ainstein-radar-drivers
Requires:       ros-melodic-ainstein-radar-filters
Requires:       ros-melodic-ainstein-radar-gazebo-plugins
Requires:       ros-melodic-ainstein-radar-msgs
Requires:       ros-melodic-ainstein-radar-rviz-plugins
Requires:       ros-melodic-ainstein-radar-tools
BuildRequires:  ros-melodic-catkin

%description
ROS support for Ainstein radar sensors.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Tue Nov 12 2019 Nick Rotella <nick.rotella@ainstein.ai> - 2.0.1-1
- Autogenerated by Bloom

