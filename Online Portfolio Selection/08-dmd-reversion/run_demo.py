"""The four variants, on synthetic data.

    python run_demo.py                     # noise
    python run_demo.py --signal reversal   # with a planted one-day reversal
    python run_demo.py --quick             # faster, fewer days and draws
"""
from __future__ import annotations

import argparse

from dmd_reversion.pipeline import COST, WIN, format_table, run_variants


def main() -> int:
    ap = argparse.ArgumentParser(description="DMD reversion demo on synthetic data")
    ap.add_argument("--signal", choices=["none", "reversal"], default="none")
    ap.add_argument("--rank", type=int, default=20, help="0 means full rank")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    print("=" * 66)
    print("SYNTHETIC DATA -- generated in this repository. No economic meaning.")
    print(f"signal={args.signal}  rank={'full' if args.rank == 0 else args.rank}  "
          f"cost={COST:.0%}  win threshold={WIN:.0%}")
    print("=" * 66)

    print(format_table(run_variants(args.signal, args.quick, args.rank or None, args.seed)))

    break_even = (COST + WIN) / (2 * WIN)
    print(f"\na win nets {WIN - COST:+.0%}, a loss costs {-WIN - COST:+.0%}, "
          f"so break-even is a {break_even:.0%} win rate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
