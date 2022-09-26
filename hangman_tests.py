


import unittest



import hangman as hangman





class TestHangmanProgram(unittest.TestCase):


	def test_select_random_word(self):

		# probably not the most robust way to test
		# this, but good enough
		# generate 100 random words and
		for i in range(0, 100):
			word = hangman.HangmanGame.select_random_word()
			for letter in word:
				if( ord(letter) < 97 or ord(letter) > 122):
					self.assertTrue(False)

	# def test_make_string_lower_case(self):

	# 	let = hangman.HangmanGame.make_string_lower_case("A")
	# 	self.assertEqual("a", let)

	# 	let = hangman.HangmanGame.make_string_lower_case("a")
	# 	self.assertEqual("a", let)

	# 	word = hangman.HangmanGame.make_string_lower_case("LIZARD")
	# 	self.assertEqual("lizard", word)

	# 	word = hangman.HangmanGame.make_string_lower_case("lizard")
	# 	self.assertEqual("lizard", word)

	# 	word = hangman.HangmanGame.make_string_lower_case("aB c&xYZ")
	# 	self.assertEqual("ab c&xyz", word)



	def test_HangmanGameClass(self):

		hmg = hangman.HangmanGame(debugging_word = "luxury")

		self.assertEqual("luxury", hmg.get_secret_word())
		self.assertFalse(hmg.is_game_over())
		self.assertFalse(hmg.check_letter_already_guessed("z"))
		self.assertFalse(hmg.process_letter_guess("b"))
		self.assertFalse(hmg.process_word_guess("funny"))
		self.assertEqual("['_', '_', '_', '_', '_', '_']", str(hmg))


		# change the state, and re-run several tests
		self.assertTrue(hmg.process_letter_guess("x"))
		self.assertEqual("['_', '_', 'x', '_', '_', '_']", str(hmg))
		self.assertTrue(hmg.check_letter_already_guessed("x"))
		self.assertFalse(hmg.is_game_over())


		# change the state with uppercase letter
		self.assertTrue(hmg.process_letter_guess("U"))
		self.assertEqual("['_', 'u', 'x', 'u', '_', '_']", str(hmg))
		self.assertTrue(hmg.check_letter_already_guessed("x"))
		self.assertFalse(hmg.is_game_over())


		# solve the puzzle by guessing all letters
		hmg.process_letter_guess("l")
		hmg.process_letter_guess("r")
		hmg.process_letter_guess("y")
		self.assertTrue(hmg.is_game_over())


		hmg = hangman.HangmanGame(debugging_word="luxury")
		# solve the puzzle by guessing word
		self.assertTrue(hmg.process_word_guess("luxury"))
		self.assertTrue(hmg.is_game_over())

		hmg = hangman.HangmanGame(debugging_word="luxury")
		# finish the game by guessing too many wrong letters
		hmg.process_letter_guess("a")
		hmg.process_letter_guess("b")
		hmg.process_letter_guess("c")
		hmg.process_letter_guess("d")
		hmg.process_letter_guess("e")
		hmg.process_letter_guess("f")
		self.assertFalse(hmg.is_game_over())
		hmg.process_letter_guess("g")
		self.assertTrue(hmg.is_game_over())




	def test_GallowsAndLittleGuyClass(self):

		lg = hangman.GallowsAndLittleGuy()
		#print(lg)
		self.assertEqual('''+----+
|    |
|
|
|
|
|
+---------''', str(lg))

		lg.add_body_part()
		self.assertEqual('''+----+
|    |
|    0
|
|
|
|
+---------''', str(lg))

		lg.add_body_part()
		lg.add_body_part()
		lg.add_body_part()
		lg.add_body_part()
		lg.add_body_part()
		self.assertEqual('''+----+
|    |
|    0
|  --+--
|    |
|   / \\
|
+---------''', str(lg))

		lg.add_body_part()
		self.assertEqual('''+----+
|    |
|    0
|  --+--
|    |
|   / \\
|
+---------''', str(lg))



if __name__ == '__main__':
	unittest.main()