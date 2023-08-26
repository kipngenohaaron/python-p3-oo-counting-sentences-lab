#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value = ""):
    self.value = value

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
   if not self.value:
     return 0
   sentences = [sentence.strip() for sentence in self.value.split(".") if sentence.strip()]
   return len(sentences)  