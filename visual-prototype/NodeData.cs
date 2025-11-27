using Godot;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;

public readonly record struct FunctionNode(Guid Id, NodeType Tag, Vector2 Position)
{
	public ImmutableArray<PinConfig> GetArgPins() => Tag switch
	{
		NodeType.PRINT => [new PinConfig("input", VariableType.ANY)],

		NodeType.CONSTANT => ImmutableArray<PinConfig>.Empty,

		NodeType.LOGICAL_AND => [
				new PinConfig( "in_a", VariableType.BOOL),
				new PinConfig( "in_b", VariableType.BOOL)
			   ],

		NodeType.LOGICAL_OR => [
			new PinConfig( "in_a", VariableType.BOOL),
			new PinConfig( "in_b", VariableType.BOOL)
		   ],
	};

	public ImmutableArray<PinConfig> GetResultPins() => Tag switch
	{
		NodeType.PRINT => ImmutableArray<PinConfig>.Empty,

		NodeType.VAR_READ => [new PinConfig("data", VariableType.BOOL)],
		NodeType.VAR_WRITE => ImmutableArray<PinConfig>.Empty,

		NodeType.LOGICAL_AND => [new PinConfig("out", VariableType.BOOL)],

		NodeType.LOGICAL_OR => [new PinConfig("out", VariableType.BOOL)],
	};

	public void GenerateResults(Board board, Dictionary<string, RefVar> userVariableTable)
	{
		switch (Tag)
		{
			case NodeType.PRINT:
				{
					
				}

			_: throw new Exception();
		}
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
