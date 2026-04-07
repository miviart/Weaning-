<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:padding="16dp">

    <CheckBox android:id="@+id/check_mejoria"
        android:text="Mejoría del proceso" />

    <CheckBox android:id="@+id/check_hemo"
        android:text="Estabilidad hemodinámica" />

    <CheckBox android:id="@+id/check_oxi"
        android:text="Oxigenación adecuada" />

    <CheckBox android:id="@+id/check_consciente"
        android:text="Despierto/colaborador" />

    <Button
        android:id="@+id/btnEvaluar"
        android:text="Evaluar PVE" />

    <TextView
        android:id="@+id/result"
        android:textSize="18sp" />

</LinearLayout>