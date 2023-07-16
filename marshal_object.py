import marshal

def main():
  """Creates a sample marshal object.
  """

  list_object = [1, 2, 3]
  marshaled_object = marshal.dumps(list_object)
  with open("marshaled_object.pcy", "wb") as f:
    f.write(marshaled_object)

if __name__ == "__main__":
  main()