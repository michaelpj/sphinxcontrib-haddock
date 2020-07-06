{ lib, buildPythonPackage, sphobjinv, sphinxcontrib-domaintools }:

buildPythonPackage rec {
  pname = "sphinxcontrib-sphinxhaddock";
  version = "0.1";

  src = ./.;
  
  propagatedBuildInputs = [ sphobjinv sphinxcontrib-domaintools];

  doCheck = false;

  meta = with lib; {
    homepage = "";
    description = "";
    license = licenses.mit;
    maintainers = with maintainers; [ michaelpj ];
  };
}
