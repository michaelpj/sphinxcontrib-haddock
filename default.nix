let
  pkgs = import <nixpkgs> {};
in {
  inherit pkgs;
  sphobjinv = pkgs.python35.pkgs.callPackage ./sphobjinv.nix {};
}
