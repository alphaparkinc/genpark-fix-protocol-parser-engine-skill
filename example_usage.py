from client import FIXProtocolParser

def main():
    print("=== Testing FIX Protocol Parser ===")
    parser = FIXProtocolParser()

    msg = "8=FIX.4.4\x0135=8\x0137=ORDER-12345\x0138=100\x0144=150.25\x0110=128\x01"
    res = parser.parse_message(msg)

    print("Parsed FIX Message Fields:")
    for tag, val in res.items():
        print(f"  Tag {tag} = {val}")

    assert res["35"] == "8" # Execution Report
    assert res["37"] == "ORDER-12345"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
