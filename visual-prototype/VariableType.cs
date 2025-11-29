#region Base
public abstract class UserVariable;
public class VariableAny : UserVariable;
#endregion

#region Value Types
public abstract class UserVariableValue : VariableAny;
public class VariableNothing : UserVariableValue;
public sealed class VariableBool : UserVariableValue
{
    public bool Value { get; }

    public VariableBool(bool value)
    {
        Value = value;
    }
}

public sealed class VariableInt : UserVariableValue
{
    public int Value { get; }

    public VariableInt(int value)
    {
        Value = value;
    }
}
public sealed class VariableString : UserVariableValue
{
    public string Value { get; }

    public VariableString(string value)
    {
        Value = value;
    }
}
#endregion

#region Collection Types
/// All collections can only have one type and cannot have collections inside them

public abstract class UserVariableCollection<T> : VariableAny where T : UserVariableValue;
public sealed class VariableVector<T> : UserVariableCollection<T> where T : UserVariableValue
{
    public T[] Array { get; }
    public int Length { get; }
    public VariableVector(T[] items)
    {
        Array = items;
        Length = Array.Length;
    }
}

public sealed class VariableMatrix<T> : UserVariableCollection<T> where T : UserVariableValue
{
    public T[,] Matrix { get; }
    public int Height => Matrix.GetLength(0);
    public int Width => Matrix.GetLength(1);


    public VariableMatrix(T[,] items)
    {
        Matrix = items;
    }
}
#endregion


