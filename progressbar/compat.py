
try:
  next
except NameError:
    def next(iter):
        try:
            # Try new style iterators
            return iter.__next__()
        except AttributeError:
            # Fallback in case of a "native" iterator
            return iter.next()


# Python < 2.5 does not have "any"
try:
  any
except NameError:
   def any(iterator):
      for item in iterator:
         if item: return True
      return False
