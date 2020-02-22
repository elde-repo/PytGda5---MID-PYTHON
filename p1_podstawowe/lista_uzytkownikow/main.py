from users_data import UsersData

if __name__ == "__main__":
    ud = UsersData()

    ud.add_user("Si", "Nowak")
    ud.add_user("Bartek", "Miler", "barmil", "997")
    # ud.add_user(**ud.users[0])
    ud.remove_user(10)

    # ud.print_users()
    print(ud)
