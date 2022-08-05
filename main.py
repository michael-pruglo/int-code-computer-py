from IntCodeImpl import IntCode

if __name__ == "__main__":
    ic = IntCode()
    ic.set_mem([3,3,1107,-1,8,3,4,3,99])
    ic.set_input([55])
    ic.exec(verbose=True)

    print()
    print(f"value =  {ic.get_val()}")
    print(f"output = {ic.get_output()}")
