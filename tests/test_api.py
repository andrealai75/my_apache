import os

def package_is_installed(name):
  os.system('dpkg -l | apache2')

def test_apache_installed():
    assert package_is_installed('apache2') == 'ss'
