# Example: Crypto CTF Workflow

## Challenge Type

ECDSA signature challenge.

## Known Information

Two signatures may share the same nonce value. If the same `r` appears in two ECDSA signatures, the private key may be recoverable.

## Agent Workflow

1. Extract curve parameters.
2. Extract message hashes.
3. Compare signature `r` values.
4. Derive nonce `k`.
5. Recover private key `d`.
6. Sign target message.
7. Submit forged signature.

## Formula

Given two signatures:

```text
s1 = k^-1 * (z1 + r * d) mod n
s2 = k^-1 * (z2 + r * d) mod n
