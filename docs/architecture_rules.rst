Architecture Rules
------------------

architecture_005
################

This rule checks for the *is* keyword is on the same line as the *architecture* keyword.
Keeping the *is* on the same line reduces file length.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO
     is

   architecture RTL of FIFO

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

   architecture RTL of FIFO is


architecture_010
################

This rule checks for the keyword *architecture* in the *end architecture* statement.
It is clearer to the reader to state what is ending.

**Violation**

.. code-block:: vhdl

   end ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

architecture_024
################

This rule checks for the architecture name in the *end architecture* statement.
It is clearer to the reader to state which architecture the end statement is closing.

**Violation**

.. code-block:: vhdl

   end architecture;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;
