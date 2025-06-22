import pathlib
import sys

in_path = pathlib.Path(sys.argv[1]).resolve()

with open(in_path, mode="rb") as in_file:
	start_pos = 0
	pos = 0
	file_index = 0
	found = False

	print("Reading file...")
	while True:
		in_file.seek(pos)

		chunk = in_file.read(4)
		if not chunk:
			break

		if chunk == bytes("VAGp", "utf-8"):
			if not found:
				found = True
				start_pos = pos
			else:
				in_file.seek(start_pos)
				data = in_file.read(pos - start_pos - 1)

				with open(str(file_index) + ".vag", "wb") as out_file:
					out_file.write(data)

				print(f"Ripped {file_index}.vag")
				
				start_pos = pos
				file_index += 1

		pos += 1