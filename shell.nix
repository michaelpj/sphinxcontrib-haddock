{ pkgs ? import <nixpkgs> {} }:
let
  inherit (import ./default.nix { inherit pkgs; }) sphobjinv;
  python = pkgs.python35.withPackages (ps: [ sphobjinv ]);
in python.env
