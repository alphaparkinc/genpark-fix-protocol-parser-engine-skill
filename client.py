class FIXProtocolParser:
    """
    Financial Information eXchange (FIX) Tag-Value Parser and Validator.
    Verifies checksum (Tag 10) and parses standard fields.
    """
    def parse_message(self, fix_raw_str, delimiter="\x01"):
        fields = fix_raw_str.split(delimiter)
        parsed = {}
        for f in fields:
            if "=" in f:
                tag, val = f.split("=", 1)
                parsed[tag] = val
        if "10" in parsed:
            idx = fix_raw_str.find(f"10={parsed['10']}")
            if idx != -1:
                body_bytes = fix_raw_str[:idx].encode('ascii')
                calc_sum = sum(body_bytes) % 256
                parsed["checksum_valid"] = (int(parsed["10"]) == calc_sum)
        return parsed
