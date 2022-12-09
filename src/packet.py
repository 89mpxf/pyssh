def generate_length(num: int) -> bytes:
    return bytes([int(hex(num)[2:].rjust(8, '0')[i:i+2], 16) for i in range(0, 8, 2)])

def create_packet(packet_type: int, *fields: bytes) -> bytes:
    packet = packet_type.to_bytes(byteorder="big")
    for field in fields:
        packet += generate_length(len(field)) + field
    return generate_length(len(packet)) + int(padding_length := 16 - (len(packet) % 16)).to_bytes(byteorder="big") + packet + (b'\x00' * padding_length)