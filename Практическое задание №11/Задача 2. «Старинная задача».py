for bull in range(0, 11):
    for cow in range(0, 21):
        remaining = 200 - 20 * bull - 10 * cow

        if remaining >= 0:
            calves = remaining

            if bull + cow + calves >= 1:
                print(f"Быков: {bull}, коров: {cow}, телят: {calves}")