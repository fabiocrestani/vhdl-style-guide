Type Rules
----------

type_001
########

This rule checks the indent of the **type** declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

       type state_machine is (IDLE, WRITE, READ, DONE);

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     type state_machine is (IDLE, WRITE, READ, DONE);

   begin

type_002
########

This rule checks the **type** keyword has proper case.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   TYPE state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_003
########

This rule checks for spaces after the **type** keyword.

**Violation**

.. code-block:: vhdl

   type   state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

.. NOTE:: The number of spaces after the **signal** keyword is configurable.
   Use the following YAML file example to change the default number of spaces.

   .. code-block:: yaml

   rule:
     type_003:
         spaces: 3 

type_004
########

This rule checks the type name has proper case.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   type STATE_MACHINE is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_005
########

This rule checks the indent of multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (
   IDLE,
     WRITE,
   READ,
      DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE);

type_006
########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine    is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_007
########

This rule checks for a single space after the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine is     (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_008
########

This rule checks the closing parenthesis of multiline enumerated types is on it's own line.

**Violation**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE
   );

type_009
########

This rule checks for an enumerate type after the open parenthesis on multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (IDLE,
     WRITE,
     READ,
     DONE
   );

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE
   );

type_010
########

This rule checks for a blank line above the **type** declaration.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   type state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

   type state_machine is (IDLE, WRITE, READ, DONE);

type_011
########

This rule checks for a blank line below the **type** declaration.

**Violation**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);
   signal sm : state_machine;

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

   signal sm : state_machine;

type_012
########

This rule checks the indent of record elements in record types.

**Violation**

.. code-block:: vhdl

   type interface is record
     data : std_logic_vector(31 downto 0);
   chip_select : std_logic;
       wr_en : std_logic;
   end record;

**Fix**

.. code-block:: vhdl

   type interface is record
     data : std_logic_vector(31 downto 0);
     chip_select : std_logic;
     wr_en : std_logic;
   end record;

type_013
########

This rule checks the **is** keyword in type definitions has proper case.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   type interface IS record
   type interface Is record
   type interface is record

**Fix**

.. code-block:: vhdl

   type interface is record
   type interface is record
   type interface is record

type_014
########

This rule checks for consistent capitalization of type names.

**Violation**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

   signal sm : State_Machine;

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

   signal sm : state_machine;

type_015
##########

This rule checks for valid prefixes in user defined type identifiers.

.. NOTE:: The default new type prefix is "t\_".

   Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   type my_type is range -5 to 5 ;

**Fix**

.. code-block:: vhdl

   type t_my_type is range -5 to 5 ;
