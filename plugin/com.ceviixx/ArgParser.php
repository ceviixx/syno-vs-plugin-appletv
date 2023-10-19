<?php
//##################################################################
// Argparse.php
// Author: Jan Koci
// Date: 26.2.2018
// Brief: Command line arguments parser for php based on argparse for Python
//##################################################################

/**
 * Class representing the parser
 */
class ArgParser
{
  private $arguments;
  private $arg_vec;
  private $usage;
  private $arg_count;

  function __construct($usage='')
  {
    global $argv;
    $this->argumets = array();
    $this->arg_vec = $argv;
    $this->arg_count = count($argv);
    $this->usage = $usage;
  }

  // method to add new argument to the parser
  public function add_argument($name, $help='', $action='get_val')
  {

    if ($action == "get_val") {
      $regex = '/^-?-?'.$name.'(=[^\s]*)?$/';
    }
    // for other actions is the same regular expression
    else {
      $regex = '/^-?-?'.$name.'$/';
    }
    // create new argument
    $argument = new Arg($name, $help, $action, $regex);
    array_push($this->argumets, $argument);
  }

  // method to parse command line arguments
  public function parse()
  {
    $ret_args = array();

    foreach ($this->argumets as $arg) {
      // find matches in argv
      $match = preg_grep($arg->regex, $this->arg_vec);

      if ($match) {
        $index = array_keys($match);
        if (count($index) > 1) {
          print("ERROR: argument '$arg->name' cannot be used more than once\n");
          exit(10);
        }
        $index = $index[0];

        // remove the first --
        $name = str_replace("-", "", $arg->name);

        switch ($arg->action) {
          case 'store_true':
            $ret_args[$name] = true;
            unset($this->arg_vec[$index]);
            break;

          case 'store_false':
            $ret_args[$name] = false;
            unset($this->arg_vec[$index]);
            break;

          case 'get_val':
            $data = explode('=', $match[$index]);

            if (count($data) == 1) {
              $next_arg = $this->arg_vec[$index+1];
              if (!$next_arg) {
                print("ERROR: argument '$arg->name' requires a value\n");
                exit(10);
              }
              $value = $next_arg;
              unset($this->arg_vec[$index+1]);
            }
            else {
              $value = $data[1];
            }
            $ret_args[$name] = $value;
            unset($this->arg_vec[$index]);
            break;

          case 'print_help':
            if ($this->arg_count > 2) {
              print("ERROR: Argument --help cannot be used with any other argument\n");
              exit(10);
            }
            $this->print_help();
            exit(0);
        }
      }
    }

    if (count($this->arg_vec) != 1) {
      print("ERROR: unknown arguments\n");
      exit(10);
    }
    return $ret_args;
  }

  public function print_help()
  {
    print($this->usage); echo "\n\n";
    foreach ($this->argumets as $arg) {
      if (strlen($arg->name) > 15)
      {
        $tabs = "\t";
      }
      elseif (strlen($arg->name) > 7){
        $tabs = "\t\t";
      }
      else {
        $tabs = "\t\t\t";
      }
      print($arg->name.$tabs.$arg->help); echo "\n";
    }
  }

}

/**
 * Class representing command line argument
 */
class Arg
{
  public $name;
  public $help;
  public $action;
  public $regex;

  function __construct($name, $help, $action, $regex)
  {
    $this->name = $name;
    $this->help = $help;
    $this->action = $action;
    $this->regex = $regex;
  }
}

  // _____________USAGE_____________
  // $message = "USAGE: php ArgParser.php [--source=filename] [--help]";
  // $parser = new ArgParser($usage=$message);
  // $parser->add_argument('source', $help="source filename", $action='get_val');
  // $parser->add_argument("help", $help="print help message", $action='print_help');
  // $parser->add_argument("f", $help="a random flag", $action='store_true');
  // $args = $parser->parse();
  // print_r($args);
?>
