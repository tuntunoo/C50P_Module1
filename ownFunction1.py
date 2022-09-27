def main():
    x=input()
    print(convert(x))

def convert(n):
    return n.replace(":)","🙂").replace(":(","🙁")

main()
  