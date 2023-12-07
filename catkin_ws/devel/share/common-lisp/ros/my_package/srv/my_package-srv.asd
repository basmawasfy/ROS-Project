
(cl:in-package :asdf)

(defsystem "my_package-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddtwoInts" :depends-on ("_package_AddtwoInts"))
    (:file "_package_AddtwoInts" :depends-on ("_package"))
  ))