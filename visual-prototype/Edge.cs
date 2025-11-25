using System.Collections.Immutable;

public readonly record struct Edge(PinAddress Source, ImmutableArray<PinAddress> Sinks);
