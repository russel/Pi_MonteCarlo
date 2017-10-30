import std.algorithm: reduce;
import std.random: uniform01;
import std.range: iota;
import std.stdio: writefln;
import core.time: MonoTime;

uint f() {
	auto immutable x = uniform01!(double)();
	auto immutable y = uniform01!(double)();
	return (x * x + y * y <= 1.0) ? 1 : 0;
}

int main() {
	immutable n = 10_000_000;
	immutable startTime = MonoTime.currTime;
	immutable pi = 4.0 * reduce!((t, x) => t + f())(0, n.iota) / n;
	immutable elapseTime = (MonoTime.currTime - startTime).total!"hnsecs" * 100e-9;
	writefln("\tSequential Reduce π ≅ %.11f, calculated in %.2fs, using %d points.", pi, elapseTime, n);
	return 0;
}

// ldc2 1.4.0 has a problem with %,d format specifier.
