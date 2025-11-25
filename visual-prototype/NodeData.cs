using Godot;
using System;
using System.Collections.Immutable;

public readonly record struct NodeData(Guid Id, NodeType Tag, Vector2 Position)
{
	public ImmutableArray<PinAddress> GetArgPins() => Tag switch
	{
		NodeType.PRINT => [new PinId(Id, "input", VariableType.STRING)],

		NodeType.CONSTANT => ImmutableArray<PinAddress>.Empty,

		NodeType.LOGICAL_AND => [
				new PinId(Id, "in_a", VariableType.BOOL),
				new PinId(Id, "in_b", VariableType.BOOL)
			   ],

		NodeType.LOGICAL_OR => [
			new PinId(Id, "in_a", VariableType.BOOL),
			new PinId(Id, "in_b", VariableType.BOOL)
		   ],
	};

	public ImmutableArray<PinAddress> GetResultPins() => Tag switch
	{
		NodeType.PRINT => ImmutableArray<PinAddress>.Empty,

		NodeType.CONSTANT => [new PinId(Id, "data", VariableType.BOOL)],

		NodeType.LOGICAL_AND => [new PinId(Id, "out", VariableType.BOOL)],

		NodeType.LOGICAL_OR => [new PinId(Id, "out", VariableType.BOOL)],
	};

	public void GenerateResults()
	{
		GD.Print($"GENERATE RESULTS FOR: {this}"); // TODO PLACEHOLDER
												   // Pattern match on type -> return node's result}
	}
	public object GetResult() => Tag switch
	{
		NodeType.PRINT => null,  // TODO nothing type?

		NodeType.CONSTANT => "PLACEHOLDER!!",

		NodeType.LOGICAL_AND => throw new NotImplementedException(),

		NodeType.LOGICAL_OR => throw new NotImplementedException(),
	};

	public bool HasOutput() => GetResult() is not null; // TODO nothing type?
}
