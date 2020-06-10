{ lib, buildPythonPackage, fetchPypi, attrs, certifi, fuzzywuzzy, jsonschema }:

buildPythonPackage rec {
  pname = "sphobjinv";
  version = "2.0.1";

  src = fetchPypi {
    inherit pname version;
    sha256 = "126lgm54c94ay3fci512ap4l607gak90pbz0fk98syxvj5izrrzx";
  };
  
  propagatedBuildInputs = [ attrs certifi fuzzywuzzy jsonschema ];

  doCheck = false;

  meta = with lib; {
    homepage = "https://github.com/bskinn/sphobjinv";
    description = "";
    license = licenses.mit;
    maintainers = with maintainers; [ michaelpj ];
  };
}
