using System;
using System.Collections.ObjectModel;

public readonly record struct BoardConfig
(
	ReadOnlyDictionary<Guid, BaseNode> Nodes,
	ReadOnlyDictionary<PinAddress, Edge> Edges,
	ReadOnlyDictionary<PinAddress, VariableAny> EmbeddedVariables,
	ReadOnlyDictionary<string, VariableAny> InitialUserVariables
);