const input = await Deno.readTextFile('15.txt');

const MOVE_MAP = {
	'^': [0, -1],
	'>': [1, 0],
	'v': [0, 1],
	'<': [-1, 0],
}

function parse(input: string) {
	const grid = input.split('\n\n')[0].split('\n').map(line => line.split(''));
	const moves = input.split('\n\n')[1].replaceAll('\n', '');
	return [grid, moves] as const;
}

function part1(grid: string[][], moves: string) {
	grid = grid.map(line => line.slice());

	let posY = grid.findIndex(line => line.includes('@')), posX = grid[posY].indexOf('@');

	for (const [moveX, moveY] of [...moves].map(move => MOVE_MAP[move as '^' | '>' | 'v' | '<'])) {
		const newPosX = posX + moveX, newPosY = posY + moveY;
		let finalPosX = newPosX, finalPosY = newPosY;
		while (grid[finalPosY][finalPosX] === 'O') {
			finalPosX += moveX;
			finalPosY += moveY;
		}
		if (grid[finalPosY][finalPosX] === '#') continue;
		grid[posY][posX] = '.';
		grid[finalPosY][finalPosX] = 'O';
		grid[newPosY][newPosX] = '@';
		posX = newPosX;
		posY = newPosY;
	}

	return grid.reduce((acc0, line, y) => acc0 + line.reduce((acc1, c, x) => c === 'O' ? acc1 + 100 * y + x : acc1, 0), 0);
}

console.log(part1(...parse(input)));
