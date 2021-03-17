

layout(location = 0) out vec4 BackBuffer;


void main()
{
	BackBuffer = vec4(abs(gl_FragCoord.xy) / vec2(800.0, 600.0), 0.0, 1.0);
}