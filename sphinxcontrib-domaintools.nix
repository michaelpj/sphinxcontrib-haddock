{ lib, buildPythonPackage, fetchPypi, sphinx }:

buildPythonPackage rec {
  pname = "sphinxcontrib-domaintools";
  version = "0.3";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1bb3c920y9gbwjcrdlf8pv6vja8sar3kfysndnkhd020nnw36zjx";
  };

  propagatedBuildInputs = [ sphinx ];

  doCheck = false;

  meta = with lib; {
    homepage = "https://github.com/sphinx-contrib/domaintools";
    description = "";
    maintainers = with maintainers; [ michaelpj ];
  };
}
