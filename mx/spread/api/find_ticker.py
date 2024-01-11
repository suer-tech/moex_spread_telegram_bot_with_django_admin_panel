def main():
    with Client(TOKEN) as client:
        inst = client.instruments.find_instrument(query='MGNT')
        print(inst)
        for cur in inst.instruments:
            print(cur)
            print('')
main()