import sys
import requests

def main():
    try:
        bitcoins = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r.raise_for_status()
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Plese enter amount of bitcoins you want to buy")
    except requests.exceptions.RequestException as e:
        sys.exit("There was an error doing the request")
    
    r_json = r.json()
    bitcoin_rate = get_bitcoin_rate(r_json)
    costs = caculate_cost(bitcoins, bitcoin_rate)
    costs = format_cost(costs)
    print(costs)

def caculate_cost(bitcoins, rate):
    return bitcoins * rate

def format_cost(costs):
    return f"${costs:,.4f}"

def get_bitcoin_rate(json_data):
    return json_data["bpi"]["USD"]["rate_float"]

def get_json(r):
    return r.json()

if __name__ == "__main__":
    main()