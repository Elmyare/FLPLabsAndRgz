(defun delete-first-n-elements (n lst)
  (if (<= n 0)
      lst
      (if (null lst)
          nil
          (delete-first-n-elements (- n 1) (cdr lst)))))