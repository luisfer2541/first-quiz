Con el fin de afianzar la seguridad en la aplicación de paneles solares tomando como referencia el estandar OWASP Top 10 2021, las medidas que se deben tomar son las siguientes:

1. Inyección de SQL

Se debe garantizar de que todas las consultas SQL sean parametrizadas o se implemente un ORM (Object-Relational Mapping) para evitar la inyección de SQL en la base de datos MySQL. De igual manera se debe validar y corregir todas las entradas de usuario antes de realizar consultas SQL.

2. Autenticación Rota

Se debe asegurar de que las contraseñas se almacenen de forma segura utilizando técnicas de almacenamiento seguro, como el uso de hashing y salting. Igualmente es importante implementar una política de contraseñas seguras y permitir la autenticación de dos factores (2FA) para proteger las cuentas de usuario. Por utlimo se recomienda realizar pruebas de fuerza bruta y bloquear cuentas después de un número específico de intentos fallidos.

3. Exposición de Datos Sensibles

Ratificar de que solo los usuarios autorizados puedan acceder a datos confidenciales. Por lo anterior es recomendable utilizar permisos y políticas de acceso adecuadas para restringir el acceso a información sensible dentro de la base de datos y encriptar los datos sensibles tanto en reposo como en tránsito.

4. XML External Entity (XXE)

Es importante validar y restringir las entradas XML para evitar ataques XXE en las solicitudes que involucran XML. Ademas se deben utilizar librerías de análisis XML seguras que eviten la expansión de entidades externas no confiables.

5. Rotura de Control de Acceso

Implementar un sistema de control de acceso adecuado que asegure que los usuarios solo tengan acceso a los recursos y datos autorizados.

6. Deserialización Insegura

Validar y verificar todas las entradas y datos deserializados para evitar ataques de deserialización insegura y
coartar las operaciones de deserialización a lo esencial y evitar la deserialización de datos no confiables.

7. Expresiones Regulares Catastróficas (Regular Expression DoS)

Evitar el uso de expresiones regulares complejas que puedan provocar ataques de denegación de servicio en la validación de entrada. De igual manera se debe corroborar y limitar las entradas de usuario que involucran expresiones regulares.

8. Seguridad de Componentes con Problemas (Security Misconfiguration)

Revisar la configuración de seguridad de los contenedores Kubernetes, servicios de AWS y aplicaciones para garantizar que estén correctamente configurados y actualizados. Igualmente se deben implementar políticas de seguridad que restrinjan el acceso innecesario a los componentes y sistemas.

9. Cross-Site Scripting (XSS)

Ratificar y escapar adecuadamente todas las salidas de usuario para prevenir ataques XSS en la aplicación web escrita en JavaScript con Next.js.

10. Redirecciones y Reenvíos no Validados (Unvalidated Redirects and Forwards)

Validar y verificar todas las redirecciones y reenvíos para evitar ataques de suplantación y redirección no autorizada. Además, es importante implementar prácticas de seguridad y políticas de acceso que se ajusten a los roles de los empleados. Esto incluye el principio de menor privilegio, lo que significa que cada usuario o empleado debe tener el nivel de acceso mínimo necesario para realizar sus tareas.

De manera general es importante realizar pruebas de seguridad y auditorías regulares en la aplicación para identificar y solucionar posibles vulnerabilidades.