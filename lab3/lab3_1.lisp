(defun member-of-set (element set)
  (cond
    ((null set) nil)
    ((equal element (car set)) t)
    (t (member-of-set element (cdr set)))))

(defun sets-equal (set1 set2)
  (and (m-subsetp set1 set2) (subsetp set2 set1)))

(defun m-subsetp (set1 set2)
  (cond
    ((null set1) t)
    ((member-of-set (car set1) set2) (m-subsetp (cdr set1) set2))
    (t nil)))

;; Пример использования:
(sets-equal '(1 2 3) '(3 1 2))
(sets-equal '(1 2 3) '(3 4 5))
