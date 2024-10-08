import sys
import requests

def main():
    try:
        bitcoins = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if not r: raise requests.RequestException("There was an error doing the request")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Plese enter amount of bitcoins you want to buy")
    except requests.exceptions.RequestException as e:
        sys.exit(e)
    
    r_json = r.json()
    bitcoin_rate = r_json["bpi"]["USD"]["rate_float"]
    costs = bitcoins * bitcoin_rate
    print(f"${costs:,.4f}")
if __name__ == "__main__":
    main()