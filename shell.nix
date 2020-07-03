{ pkgs ? import <nixpkgs> {} }:
let
  inherit (import ./default.nix { inherit pkgs; }) sphobjinv sphinxcontrib-domaintools;
  python = pkgs.python35.withPackages (ps: [ sphobjinv sphinxcontrib-domaintools ]);
in python.env
