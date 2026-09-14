#!/usr/bin/env python3
# TBH-ParamFinder - Bug Bounty Hidden Parameter Finder
import requests, argparse, json, re

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-ParamFinder \033[91m- Bug Bounty      \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

COMMON = ["id","page","q","search","lang","url","redirect","next","debug","test","admin","user","file","path","view","cat","dir","order","sort","filter"]

def find_params(url):
    try:
        r=requests.get(url,timeout=5,headers={'User-Agent':'TBH-ParamFinder/1.0'})
        # Find params in JS and HTML
        params=set(re.findall(r"[?&](\w+)=|\"(\w+)\":|param[=|:]\s*['\"](\w+)", r.text))
        # Flatten
        flat=set()
        for tup in params:
            for p in tup:
                if p and len(p)>2: flat.add(p)
        # Intersect with COMMON
        found=[p for p in COMMON if p.lower() in r.text.lower()]
        return {"url":url,"status":r.status_code,"found_common":found,"found_all":list(flat)[:10]}
    except Exception as e:
        return {"url":url,"error":str(e)}

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="ParamFinder")
    parser.add_argument("-u","--url",required=True,help="Target URL")
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    print(f"[*] Scanning {args.url} untuk hidden params...")
    result=find_params(args.url)
    print(f"[+] Status: {result.get('status')}")
    print(f"[+] Common params found: {result.get('found_common')}")
    print(f"[+] All hints: {result.get('found_all')}")
    print("\n-> Coba: ?id=1, ?debug=true, ?admin=true untuk cari IDOR/XSS")
    if args.json:
        open(args.json,'w').write(json.dumps(result,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
