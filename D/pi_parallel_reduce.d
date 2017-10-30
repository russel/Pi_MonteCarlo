import std.algorithm: map;
import std.parallelism: taskPool, totalCPUs;
import std.random: uniform01;
import std.range: iota;
import std.stdio: writefln;
import core.time: MonoTime;

uint f(int i) {
	auto immutable x = uniform01!(double)();
	auto immutable y = uniform01!(double)();
	return (x * x + y * y <= 1.0) ? 1 : 0;
}

int main() {
	immutable n = 10_000_000;
	immutable startTime = MonoTime.currTime;
	immutable pi = 4.0 * taskPool.reduce!"a + b"(n.iota.map!(f)) / n;
	immutable elapseTime = (MonoTime.currTime - startTime).total!"hnsecs" * 100e-9;
	writefln("\tParallel Reduce π ≅ %.11f, calculated in %.2fs, using %d points, on %d CPUs.", pi, elapseTime, n, totalCPUs);
	return 0;
}

// ldc2 1.4.0 has a problem with %,d format specifier.
