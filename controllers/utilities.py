def hashingPassword(password):
    salt = [password[i] for i in range(0, len(password), 2)]
    postsalt = ''.join(salt[:len(salt) / 2])
    presalt = ''.join(salt[len(salt) / 2:])
    return (presalt + password + postsalt)
