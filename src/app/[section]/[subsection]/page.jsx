import { notFound } from 'next/navigation';
import { navConfig } from '@/config/nav';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';

function unslugify(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

export default function SubsectionPage({ params }) {
  const { section, subsection } = params;
  const navItems = navConfig.sidebarNav[section];

  if (!navItems || !navItems.find(item => item.href === `/`+section+`/`+subsection)) {
    notFound();
  }

  const title = unslugify(subsection);

  return (
    <Card className="shadow-md animate-fade-in">
      <CardHeader>
        <p className="text-sm text-muted-foreground capitalize">{unslugify(section)}</p>
        <CardTitle className="font-headline text-3xl">{title}</CardTitle>
      </CardHeader>
      <Separator className="mb-6" />
      <CardContent className="prose max-w-none text-foreground">
        <p>
          This is the page for the "{title}" subsection. The content for this page will be added later. 
          For now, enjoy this placeholder text that describes the purpose of this page within the
          Geo Navigator application.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </CardContent>
    </Card>
  );
}
