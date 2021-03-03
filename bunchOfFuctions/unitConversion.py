def gigaConvert():
        inp=int(input("no of gigabytes :"))
        if inp>=1 and inp<=999:
            print(f'{inp}x10^9 bytes')
            print(f'{inp}x10^6 kilobytes')
            print(f'{inp}x10^3 megabytes')
