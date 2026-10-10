# TBH-ParamFinder

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-ParamFinder/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-ParamFinder/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/output-JSON-orange.svg" alt="JSON">
</p>

Hidden parameter discovery. Finds query parameters the app accepts but doesn't advertise — the hunting ground for IDOR, XSS, and access-control bugs.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Does

- Probes common parameter names (`id`, `debug`, `admin`, `redirect`, `file`, `token`, …) against the target URL
- Detects acceptance by response-length / status deltas
- Outputs found parameters as JSON for the next stage of your workflow (feed them to TBH-XSS, TBH-IDOR, …)

Hidden parameters are most valuable on endpoints you already have access to (authenticated areas, API routes found in JS).

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-ParamFinder
cd TBH-ParamFinder
pip install -r requirements.txt
```

## Usage

```
usage: paramfinder.py [-h] -u URL [--json JSON]

options:
  -u, --url URL     Target URL
  --json JSON       Save JSON
```

```bash
python3 paramfinder.py -u "https://example.com/api/user" --json params.json
```

## Sample Output

```
[*] Testing https://example.com/api/user
[+] Accepted params: id, debug
[✓] JSON: params.json
```

## Authorized Use Only

Only against scopes you own or are authorized to test. Parameter fuzzing is active scanning. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-IDOR](https://github.com/TulungagungBlackHat/TBH-IDOR) — test found `id` params for access control
- [TBH-XSS](https://github.com/TulungagungBlackHat/TBH-XSS) / [TBH-SQLi](https://github.com/TulungagungBlackHat/TBH-SQLi) — test found params for injection

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
