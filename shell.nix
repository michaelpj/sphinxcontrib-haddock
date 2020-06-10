let
  inherit (import ./default.nix) pkgs sphobjinv;
  python = pkgs.python35.withPackages (ps: [ sphobjinv ]);
in python.env
