import os

def package_installed(name):
  return os.system('dpkg -l | grep ' + name)

def test_apache_installed():
    assert package_installed('vars') == 0
