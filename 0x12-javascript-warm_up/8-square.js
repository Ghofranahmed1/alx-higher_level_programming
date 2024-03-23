#!/usr/bin/node
/**
 * script that prints a square
 */
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
	  consloe.log('X'.repeat(parseInt(process.argv[2])));
  }
}
