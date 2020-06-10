{ pkgs ? import <nixpkgs> {} }:
{
  inherit pkgs;
  sphobjinv = pkgs.python35.pkgs.callPackage ./sphobjinv.nix {};
}
