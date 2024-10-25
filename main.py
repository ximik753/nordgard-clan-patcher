import pymem
import pymem.process
from pymem.exception import MemoryReadError


def main():
    pm = pymem.Pymem("Northgard.exe")

    selected_clan = int(input('Input index clan (start with 0): '))

    keys = []
    values = []

    byte = pm.read_bytes(0x76CA9F4EB4E2 + 0x2, 8)
    static_offset = int.from_bytes(byte, byteorder='little')
    unk1 = pm.read_longlong(static_offset)
    unk2 = pm.read_longlong(unk1 + 0x40)
    unk3 = pm.read_longlong(unk2 + 0x18)
    unk4 = pm.read_longlong(unk3 + 0x20)
    unk5 = pm.read_longlong(unk4 + 0x10)
    unk6 = pm.read_longlong(unk5 + 0x10)
    unk7 = pm.read_longlong(unk6 + 0x0 * 0x8 + 0x18)
    unk8 = pm.read_longlong(unk7 + 0x8)
    unk9 = pm.read_longlong(unk8 + 0x130)
    unk10 = pm.read_longlong(unk9 + 0x10)
    for i in range(60):
        try:
            unk11 = pm.read_longlong(unk10 + i * 0x8 + 0x18)
            unk12 = pm.read_longlong(unk11 + 0x138)
            unk13 = pm.read_longlong(unk12 + 0x18)
            unk14 = pm.read_longlong(unk13 + 0x18)
            unk15 = pm.read_longlong(unk14 + 0x308)
            unk16 = pm.read_longlong(unk15 + 0x230)
            unk17 = pm.read_longlong(unk16 + 0x18)
            unk18_val = pm.read_longlong(unk17 + 0x2A8)
            unk19_val = pm.read_longlong(unk18_val + 0x8)
            unk20_val = pm.read_longlong(unk19_val + 0x10)
            unk21_val = pm.read_longlong(unk20_val + selected_clan * 8 + 0x18)
            values.append(unk21_val)

            unk18 = pm.read_longlong(unk17 + 0x2C0)
            unk19 = pm.read_longlong(unk18 + 0x18)
            unk20 = pm.read_longlong(unk19 + 0x18)
            unk21 = pm.read_longlong(unk20 + 0x10)
            unk22 = pm.read_longlong(unk21 + 0x18)
            keys.append(unk22)

            # hex_number = hex(unk22)
            # print(i, hex_number)
        except MemoryReadError:
            continue

    pm.write_longlong(keys[-1] + 0x2D8, values[-1])


if __name__ == '__main__':
    main()
